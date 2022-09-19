#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_multienv_setup.cdk_multienv_setup_stack import CdkMultienvSetupStack


app = cdk.App()
CdkMultienvSetupStack(app, "cdk-multienv")

app.synth()
