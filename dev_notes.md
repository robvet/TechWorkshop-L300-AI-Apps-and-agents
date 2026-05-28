source .venv/bin/activate

python -m uvicorn chat_app:app --host 0.0.0.0 --port 8000

AgentIDs
ID: customer-loyalty:1
ID: inventory-agent:1
ID: interior-designer:1
ID: cora:1
ID: cart-manager:1


What colors of green paint do you have?
I think I’m interested in Deep Forest. How many gallons would I need to paint a medium sized bedroom?
How much of PROD0043 do you have in stock?
Let’s add two gallons to the cart, please.
Please also add one paint tray and two of your All-Purpose Wall Paint Brushes.
What items are in my cart right now?




# Build Docker Container
 az acr build --registry 2x2oywo2ju4ngcosureg --image chat-app:latest --platform linux/amd64 --file Dockerfile .

# Push container to ACR
 az containerapp registry set \
  --name app-2x2oywo2ju4ng \
  --resource-group lab-05-27 \
  --server 2x2oywo2ju4ngcosureg.azurecr.io \
  --identity system




### Container App to authenticate against your Azure Container Registry using its system-assigned managed identity for permissions to pull container image
Run ID: dt1 was successful after 2m25s
(zava-chat-app) robvetmac26:/Volumes/robvet-stuff/_vetCode/_ai/Microsoft AI Workshop/TechWorkshop-L300-AI-Apps-and-agents/src robvet$  az containerapp registry set \
>   --name app-2x2oywo2ju4ng \
>   --resource-group lab-05-27 \
>   --server 2x2oywo2ju4ngcosureg.azurecr.io \
>   --identity system

returns

System identity is already assigned to containerapp
[
  {
    "identity": "system",
    "passwordSecretRef": "",
    "server": "2x2oywo2ju4ngcosureg.azurecr.io",
    "username": ""
  }
]

### update the Container App to pull the image you pushed:
az containerapp update \
  --name app-2x2oywo2ju4ng \
  --resource-group lab-05-27 \
  --image 2x2oywo2ju4ngcosureg.azurecr.io/chat-app:latest


returns: 

{
  "id": "/subscriptions/c5e2e3c4-7b5b-4b10-b8b2-bef972d4b0d4/resourceGroups/lab-05-27/providers/Microsoft.App/containerapps/app-2x2oywo2ju4ng",
  "identity": {
    "principalId": "5600b180-354d-462a-8269-2c6dfba06fec",
    "tenantId": "9a400a8f-ece5-4478-b55b-02bc608bf281",
    "type": "SystemAssigned"
  },
  "location": "Sweden Central",
  "name": "app-2x2oywo2ju4ng",
  "properties": {
    "configuration": {
      "activeRevisionsMode": "Single",
      "dapr": null,
      "identitySettings": [],
      "ingress": {
        "additionalPortMappings": null,
        "allowInsecure": false,
        "clientCertificateMode": null,
        "corsPolicy": null,
        "customDomains": null,
        "exposedPort": 0,
        "external": true,
        "fqdn": "app-2x2oywo2ju4ng.kindsea-5820efd7.swedencentral.azurecontainerapps.io",
        "ipSecurityRestrictions": null,
        "stickySessions": null,
        "targetPort": 8000,
        "traffic": [
          {
            "latestRevision": true,
            "weight": 100
          }
        ],
        "transport": "Http"
      },
      "maxInactiveRevisions": 100,
      "registries": [
        {
          "identity": "system",
          "passwordSecretRef": "",
          "server": "2x2oywo2ju4ngcosureg.azurecr.io",
          "username": ""
        }
      ],
      "runtime": null,
      "secrets": [
        {
          "name": "applicationinsights-connection-string"
        }
      ],
      "service": null
    },
    "customDomainVerificationId": "654E5294BE41062D17BD349CC69B58180F33C40F5DC5DD1D930FC7481C2C3BE3",
    "delegatedIdentities": [],
    "environmentId": "/subscriptions/c5e2e3c4-7b5b-4b10-b8b2-bef972d4b0d4/resourceGroups/lab-05-27/providers/Microsoft.App/managedEnvironments/2x2oywo2ju4ng-cosu-cae",
    "eventStreamEndpoint": "https://swedencentral.azurecontainerapps.dev/subscriptions/c5e2e3c4-7b5b-4b10-b8b2-bef972d4b0d4/resourceGroups/lab-05-27/containerApps/app-2x2oywo2ju4ng/eventstream",
    "latestReadyRevisionName": "app-2x2oywo2ju4ng--m3o7zfx",
    "latestRevisionFqdn": "app-2x2oywo2ju4ng--0000001.kindsea-5820efd7.swedencentral.azurecontainerapps.io",
    "latestRevisionName": "app-2x2oywo2ju4ng--0000001",
    "managedEnvironmentId": "/subscriptions/c5e2e3c4-7b5b-4b10-b8b2-bef972d4b0d4/resourceGroups/lab-05-27/providers/Microsoft.App/managedEnvironments/2x2oywo2ju4ng-cosu-cae",
    "outboundIpAddresses": [
      "4.225.128.205"
    ],
    "provisioningState": "Succeeded",
    "runningStatus": "Running",
    "template": {
      "containers": [
        {
          "env": [
            {
              "name": "COSMOS_ENDPOINT"
            },
            {
              "name": "storage_account_name"
            },
            {
              "name": "DATABASE_NAME"
            },
            {
              "name": "CONTAINER_NAME"
            },
            {
              "name": "storage_container_name"
            },
            {
              "name": "APPLICATIONINSIGHTS_CONNECTION_STRING",
              "secretRef": "applicationinsights-connection-string",
              "value": ""
            },
            {
              "name": "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT"
            },
            {
              "name": "AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED"
            },
            {
              "name": "FOUNDRY_API_VERSION"
            },
            {
              "name": "gpt_deployment"
            },
            {
              "name": "gpt_api_version"
            },
            {
              "name": "embedding_deployment"
            },
            {
              "name": "embedding_api_version"
            },
            {
              "name": "phi_4_deployment"
            },
            {
              "name": "phi_4_api_version"
            },
            {
              "name": "customer_loyalty"
            },
            {
              "name": "inventory_agent"
            },
            {
              "name": "interior_designer"
            },
            {
              "name": "cora"
            },
            {
              "name": "cart_manager"
            },
            {
              "name": "handoff_service"
            }
          ],
          "image": "2x2oywo2ju4ngcosureg.azurecr.io/chat-app:latest",
          "name": "chat-app",
          "resources": {
            "cpu": 1.0,
            "ephemeralStorage": "4Gi",
            "memory": "2Gi"
          }
        }
      ],
      "initContainers": null,
      "revisionSuffix": "",
      "scale": {
        "cooldownPeriod": 300,
        "maxReplicas": 1,
        "minReplicas": 0,
        "pollingInterval": 30,
        "rules": null
      },
      "serviceBinds": null,
      "terminationGracePeriodSeconds": null,
      "volumes": null
    },
    "workloadProfileName": null
  },
  "resourceGroup": "lab-05-27",
  "systemData": {
    "createdAt": "2026-05-27T20:51:17.7864665",
    "createdBy": "admin@MngEnvMCAP190177.onmicrosoft.com",
    "createdByType": "User",
    "lastModifiedAt": "2026-05-28T14:50:02.6675623",
    "lastModifiedBy": "admin@MngEnvMCAP190177.onmicrosoft.com",
    "lastModifiedByType": "User"
  },
  "tags": {
    "CostControl": "ignore",
    "Environment": "Lab",
    "Owner": "admin@MngEnvMCAP190177.onmicrosoft.com",
    "Project": "Tech Workshop L300 - AI Apps and Agents",
    "SecurityControl": "ignore"
  },
  "type": "Microsoft.App/containerApps"


### Set model-specific endpoints variables on CA
az containerapp update \
  --name app-2x2oywo2ju4ng \
  --resource-group lab-05-27 \
  --set-env-vars \
    FOUNDRY_ENDPOINT="https://aif-2x2oywo2ju4ng.services.ai.azure.com/api/projects/proj-2x2oywo2ju4ng" \
    gpt_endpoint="https://aif-2x2oywo2ju4ng.services.ai.azure.com" \
    embedding_endpoint="https://aif-2x2oywo2ju4ng.services.ai.azure.com" \
    phi_4_endpoint="https://aif-2x2oywo2ju4ng.services.ai.azure.com"


az containerapp update \
  --name app-2x2oywo2ju4ng \
  --resource-group lab-05-27 \
  --image 2x2oywo2ju4ngcosureg.azurecr.io/chat-app:latest
