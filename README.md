# Airflow

This repository contains DAGs and source files to create autonomous pipelines on Blent infrastructure.

## Install

### Production

In production environment, you only have to get `airflow/dags` folder since you are not using local SQLite. You will have first to clone the repository on the remote server, then 

```bash
# Inside the AIRFLOW_HOME folder
git init
git remote add origin <<REPO_URL>>
git config core.sparseCheckout true
```

You must specify a `sparse-checkout` to not pull the entire repository architecture, but only the `airflow/dags` folder.

```bash
echo "airflow/dags/" >> .git/info/sparse-checkout
echo "requirements.txt" >> .git/info/sparse-checkout
git pull origin master
```

You may now want to automatically trigger a `git pull` using a CRON job.

### Local

If you want to install it locally, create a new Python environment inside root folder.

```bash
python3 -m venv venv
source venv/bin/activate
```

You then have to install dependencies and Apache Airflow.

```bash
pip install -r requirements.txt
sh install_airflow
```

Finally, run in two separate shells both webserver and scheduler.

```bash
sh scheduler.sh
sh webserver.sh
```

Visit http://localhost:12345 to view Airflow Web UI.