# Admin scripts notes

```
 python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install requests
```

- pip install requests

```
python3 delete-docs-0.py       
Deleting index: .ds-metricbeat-8.13.2-2024.09.01-000003
Failed to delete index: .ds-metricbeat-8.13.2-2024.09.01-000003. Status Code: 400
Deleting index: .internal.alerts-observability.threshold.alerts-default-000001
Successfully deleted index: .internal.alerts-observability.threshold.alerts-default-000001
Deleting index: .ds-metrics-kubernetes.controllermanager-default-2024.05.24-000002
Failed to delete index: .ds-metrics-kubernetes.controllermanager-default-2024.05.24-000002. Status Code: 400
Deleting index: .ds-logs-apm.app.cartservice-default-2024.08.03-000008
```