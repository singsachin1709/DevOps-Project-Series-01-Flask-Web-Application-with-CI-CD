from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("dashboard.html")

@app.route('/health')
def health():
    return {"status": "UP"}

@app.route('/journey')
def journey():
    return jsonify({
        "name": "Sachin Singh Patel",
        "start": "January 2025 - AWS DevOps Intern",
        "milestones": [
            "Completed AWS training (EC2, IAM, VPC, S3, Lambda)",
            "Built Flask & FastAPI apps with Docker",
            "Implemented CI/CD with Jenkins & Ansible",
            "Deployed on Kubernetes with monitoring",
            "Working on GitOps & ArgoCD"
        ],
        "current_focus": "Mastering CI/CD + GitOps on Kubernetes"
    })

@app.route('/tools')
def tools():
    return jsonify({
        "CI/CD": ["Jenkins", "GitHub Actions", "ArgoCD"],
        "Containers": ["Docker", "Podman"],
        "Kubernetes": ["kubeadm", "Minikube", "Helm"],
        "IaC": ["Terraform", "Ansible"],
        "Cloud": ["AWS (EC2, S3, IAM, Lambda)", "EKS"]
    })

@app.route('/projects')
def projects():
    return jsonify({
        "active_projects": [
            "Flask App with CI/CD on Jenkins & Docker",
            "Prometheus Monitoring Stack on K8s",
            "LAMP Stack on Docker + K8s",
            "GitOps Deployment with ArgoCD"
        ],
        "mentor_guidance": "All under Mr. Vimal Daga's mentorship"
    })

@app.route('/certifications')
def certifications():
    return jsonify({
        "in_progress": [" AWS Cloud Technical Essentials - Coursera"],
        "planned": ["Cybersecurity Essentials - Cisco Networking Academy"]
    })

@app.route('/mentorship')
def mentorship():
    return jsonify({
        "mentor": "Mr. Vimal Daga",
        "role": "DevOps Guru & World Record Holder",
        "learning_platform": "https://devopsprojects.hash13.com/",
        "impact": "Hands-on industry-ready DevOps training"
    })

@app.route('/resources')
def resources():
    return jsonify({
        "docs": {
            "Docker": "https://docs.docker.com/",
            "Kubernetes": "https://kubernetes.io/docs/",
            "Terraform": "https://developer.hashicorp.com/terraform/docs",
            "Jenkins": "https://www.jenkins.io/doc/"
        },
        "YouTube": "https://www.youtube.com/@vimaldaga",
        "LinkedIn": "https://www.linkedin.com/in/sachin-singh-patel-devops/"
    })

@app.route('/contact')
def contact():
    return jsonify({
        "name": "Sachin Singh Patel",
        "location": "Bhopal, India",
        "email": "singsachin348@gmail.com",
        "phone": "9165845146",
        "linkedin": "https://www.linkedin.com/in/sachin-singh-patel-devops/"
    })
