from flask import Flask, render_template, jsonify
from kubernetes import client, config
import os

app = Flask(__name__)

# Charger la config OpenShift depuis le pod
config.load_incluster_config()

NAMESPACE = os.getenv("NAMESPACE", "formation-openshift")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/jobs")
def get_jobs():
    batch_v1 = client.BatchV1Api()
    jobs = batch_v1.list_namespaced_job(NAMESPACE)
    result = []
    for job in jobs.items:
        result.append({
            "name": job.metadata.name,
            "status": "Complete" if job.status.succeeded else "Running" if job.status.active else "Failed",
            "start": str(job.status.start_time)
        })
    return jsonify(result)

@app.route("/api/cronjobs")
def get_cronjobs():
    batch_v1 = client.BatchV1Api()
    cronjobs = batch_v1.list_namespaced_cron_job(NAMESPACE)
    result = []
    for cj in cronjobs.items:
        result.append({
            "name": cj.metadata.name,
            "schedule": cj.spec.schedule,
            "last_schedule": str(cj.status.last_schedule_time)
        })
    return jsonify(result)

@app.route("/api/trigger-job", methods=["POST"])
def trigger_job():
    batch_v1 = client.BatchV1Api()
    job = client.V1Job(
        metadata=client.V1ObjectMeta(name="manual-job-" + os.urandom(4).hex()),
        spec=client.V1JobSpec(
            template=client.V1PodTemplateSpec(
                spec=client.V1PodSpec(
                    containers=[client.V1Container(
                        name="job",
                        image="nginxinc/nginx-unprivileged@sha256:731f382bbad9a874f9f27db9c82d9e671e603e2210386a8e2b6da36cf336fa75",
                        command=["sh", "-c", "echo Bonjour depuis mon Job OpenShift"]
                    )],
                    restart_policy="Never"
                )
            )
        )
    )
    batch_v1.create_namespaced_job(NAMESPACE, job)
    return jsonify({"status": "Job déclenché !"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
