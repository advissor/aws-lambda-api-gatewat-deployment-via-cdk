import os
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_apigateway as apigateway,
    aws_lambda as lambda_
)

# https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/README.html#apigateway-v2
class CdkMultienvSetupStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        get_handler = lambda_.Function(self, "OrderHandler",
                function_name="OrderGet",
                runtime=lambda_.Runtime.PYTHON_3_8,
                code=lambda_.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "../src")
            ),
                handler="get.lambda_handler")
        api = apigateway.RestApi(self, "order-api")


        books = api.root.add_resource("order")
        



        # backend: lambda.Function


        get_integration = apigateway.LambdaIntegration(get_handler,request_templates={"application/json": '{ "statusCode":"200" }'})

        books.add_method("GET", get_integration)