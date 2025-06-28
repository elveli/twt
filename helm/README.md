
# 🧪 Mini Helm Lab: Build, Deploy, and Upgrade a Custom Chart

## 🔧 Prerequisites
- Kubernetes cluster (minikube, kind, or real)
- `kubectl` configured
- `helm` installed (v3+)
- Optional: `helm-diff` plugin

---

## 🧩 Part 1: Create a Custom Helm Chart

```bash
helm create myapp
cd myapp
```

### Clean up default templates

```bash
rm templates/tests/* templates/hpa.yaml templates/ingress.yaml
```

---

## 📝 Part 2: Edit `values.yaml`

Replace content with:

```yaml
replicaCount: 2

image:
  repository: nginx
  tag: stable
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

appName: my-nginx
```

---

## 🧠 Part 3: Modify `templates/deployment.yaml`

Update `metadata.name` and labels:

```yaml
metadata:
  name: {{ .Values.appName }}
  labels:
    app: {{ .Values.appName }}
```

Container section:

```yaml
containers:
- name: {{ .Values.appName }}
  image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
  ports:
    - containerPort: 80
```

---

## 🚀 Part 4: Install Your Chart

```bash
helm install myapp ./ --namespace default
kubectl get pods
```

Optional: render manifests locally

```bash
helm template myapp ./
```

---

## 🔄 Part 5: Upgrade Using Modified Values

Create `values-prod.yaml`:

```yaml
replicaCount: 3
image:
  repository: nginx
  tag: latest
```

Upgrade:

```bash
helm upgrade myapp ./ -f values-prod.yaml
kubectl get deploy my-nginx
```

Optional: show diff (if plugin installed)

```bash
helm diff upgrade myapp ./ -f values-prod.yaml
```

---

## 🧪 Part 6: Roll Back

```bash
helm rollback myapp 1
```

---

## 🧹 Part 7: Uninstall

```bash
helm uninstall myapp
```

---

## 🎯 Bonus Tasks (Optional)

| Task | What You Learn |
|------|----------------|
| Add a `NOTES.txt` | Customize post-install messages |
| Add conditionals | Use `{{- if .Values.service.enabled }}` |
| Use `_helpers.tpl` | DRY up labels/metadata |
| Deploy Redis as subchart | Add `dependencies:` to `Chart.yaml` |
| CI/CD integration | GitHub Actions: `helm upgrade --install` |
| Template secrets | Use [helm-secrets](https://github.com/jkroepke/helm-secrets) + SOPS |
