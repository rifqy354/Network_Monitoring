from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__, template_folder='./template')

DEFAULT_INVENTORY = 'inventory.yaml'

# Halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint untuk menjalankan playbook Ansible - SET_IP
@app.route('/set-ip', methods=['POST'])
def set_ip():
    print("Received request for SET_IP")
    playbook = 'set_ip.yaml'  # Nama playbook dari form
    inventory = request.form.get('inventory')  # Inventory file dari form

    if not os.path.exists(inventory):
        return jsonify({"status": "error", "message": f"Inventory file {inventory} is missing."}), 400

    try:
        # Jalankan playbook Ansible menggunakan subprocess
        command = f"ansible-playbook -i {inventory} playbooks/{playbook}"
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        # Kirim hasil ke frontend
        print("Playbook executed successfully")
        return jsonify({
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })

    except Exception as e:
        print("Error executing playbook:", str(e))
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/monitoring', methods=['POST'])
def monitoring():
    print("Recieved request for MONITORING")
    playbook = 'network_monitoring.yaml'  # Nama playbook d>    inventory = request.form.get('inventory')  # Inventory file dari form
    inventory = DEFAULT_INVENTORY

    if not os.path.exists(inventory):
        return jsonify({"status": "error", "message": "Inventory are required."}), 400

    try:
        # Jalankan playbook Ansible menggunakan subprocess
        command = f"ansible-playbook -i {inventory} playbooks/{playbook}"
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        # Kirim hasil ke frontend
        print("Playbook executed successfully")
        return jsonify({
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })

    except Exception as e:
        print("Error executing playbook:", str(e))
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
