import aws_cdk as core
import aws_cdk.assertions as assertions
from cdk_multienv_setup.cdk_multienv_setup_stack import CdkMultienvSetupStack


def test_apigateway_created():
    app = core.App()
    stack = CdkMultienvSetupStack(app, "cdk-multienv-setup")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::ApiGateway::Method", {
        "HttpMethod": "GET"})

def test_lambda_created():
    app = core.App()
    stack = CdkMultienvSetupStack(app, "cdk-multienv-setup")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::Lambda::Function", {
        "FunctionName": "OrderGet"})
    
    template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": "python3.8"})
