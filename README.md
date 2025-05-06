# Tag Search & Gen AI Tools Application

<img src="Snowflake.svg" width="100">

## Overview
This Streamlit application provides various tools for searching tags and leveraging AI capabilities within Snowflake. The application includes the following features:
- Tag Search functionality
- AI-powered Question Answering
- Next Best Action recommendations using LLMs
- Multiple foundational model support

## Prerequisites
- Snowflake account with appropriate permissions
- Access to Snowflake Cortex features
- Streamlit in Snowflake enabled

## Deployment Instructions

### 1. Create Streamlit Application in Snowflake

1. Log in to your Snowflake account
2. Navigate to Streamlit
3. Click "Create Streamlit App"
4. Fill in the following details:
   - Application Name: `tag_search_genai_tools`
   - Warehouse: Select appropriate warehouse - Running on XS Warehouee will work fine
   - Database: Choose target database(ex. TAG_DB)
   - Schema: Select schema(ex. TAG_SCHEMA)

### 2. Upload Supporting Files

1. In the Streamlit application directory:
   - Upload `streamlit_app.py`
   - Upload `environment.yml`
   - Upload `Snowflake.svg`
   - Upload `Silgan_Holdings_logo.svg`
   - These files should be in the same directory as your main application

### 3. Deploy the Code

1. Copy the provided Python code into the main editor
2. Click "Run" to test the application
3. Ensure all dependencies are properly imported

### 4. Configure Permissions

1. Grant necessary permissions:
   ```sql
   GRANT USAGE ON WAREHOUSE <warehouse_name> TO ROLE <role_name>;
   GRANT USAGE ON DATABASE <database_name> TO ROLE <role_name>;
   GRANT USAGE ON SCHEMA <schema_name> TO ROLE <role_name>;

Ensure access to Snowflake Cortex:
GRANT USAGE ON FUNCTION CORTEX.COMPLETE TO ROLE <role_name>;

Features
Tag Search
Search for tags in Snowflake metadata
Case-insensitive search functionality
Results display in tabular format
Ask the LLM
Multiple foundational model support
Interactive question-answering capability
Customizable prompts
Next Best Action
AI-powered action recommendations
Multiple model selection options
Customizable instruction prompts
Usage
Select desired tool from the sidebar
Follow the interface prompts
Enter required information
View results in the main panel
Troubleshooting
Ensure all SVG files are properly uploaded
Verify Snowflake session connectivity
Check permissions for Cortex functions
Validate warehouse compute resources
Support
For issues or questions, please contact your Snowflake administrator.

Additional Notes:
- Make sure the SVG files are accessible in the same directory as your main application
- Test the application with limited data first
- Monitor warehouse credit consumption
- Consider implementing error handling for production use
- Regular maintenance and updates may be required for optimal performance

This documentation provides a basic framework for deploying and managing your Streamlit application in Snowflake. Adjust the instructions based on your specific Snowflake environment and requirements.
