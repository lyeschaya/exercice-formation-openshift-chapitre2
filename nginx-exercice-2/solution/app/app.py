from flask import Flask, jsonify
from kubernetes import client, config
import os

app = Flask(__name__)
config.load_incluster_config()
NAMESPACE = os.getenv("NAMESPACE", "formation-openshift")

@app.route("/api/config")
def get_config():
    core_v1 = client.CoreV1Api()
    
    # Lire le ConfigMap
    cm = core_v1.read_namespaced_config_map("nginx-config-2", NAMESPACE)
    
    # Lire le Secret
    secret = core_v1.read_namespaced_secret("nginx-secret-2", NAMESPACE)
    
    import base64
    return jsonify({
        "configmap": {
            "APP_MESSAGE": cm.data.get("APP_MESSAGE", "N/A")
        },
        "secret": {
            "USERNAME": base64.b64decode(secret.data.get("USERNAME", "")).decode(),
            "PASSWORD": "••••••••"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
