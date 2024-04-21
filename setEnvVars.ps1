# PowerShell script to set Azure Cognitive Services environment variables

# Ask for the Azure Cognitive Services Endpoint
$endpoint = Read-Host "Please enter your OPENAI API KEY"
# Set the Endpoint as an environment variable for the current user
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", $endpoint, [System.EnvironmentVariableTarget]::User)

# Ask for the Azure Cognitive Services Endpoint
$endpoint = Read-Host "Please enter your Azure Cognitive Services Endpoint"
# Set the Endpoint as an environment variable for the current user
[System.Environment]::SetEnvironmentVariable("AZURE_COG_ENDPOINT", $endpoint, [System.EnvironmentVariableTarget]::User)

# Ask for the Azure Cognitive Services Key
$key = Read-Host "Please enter your Azure Cognitive Services Key"
# Set the Key as an environment variable for the current user
[System.Environment]::SetEnvironmentVariable("AZURE_COG_KEY", $key, [System.EnvironmentVariableTarget]::User)

Write-Host "Environment variables set successfully."
