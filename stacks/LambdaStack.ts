import { Function, StackContext } from "sst/constructs";
import * as cdk from "aws-cdk-lib";
import * as events from "aws-cdk-lib/aws-events";
import * as targets from "aws-cdk-lib/aws-events-targets";

export function LambdaStack({ stack }: StackContext) {
  const emptyFunction = new Function(stack, "function-s3-empty", {
    handler: "packages/functions/src/main.handler",
    runtime: "python3.9",
    memorySize: 1024,
    timeout: "5 minutes",
    architecture: "x86_64"
  });

  new events.Rule(stack, "function-s3-empty-rule", {
    schedule: events.Schedule.rate(cdk.Duration.days(1)),
  }).addTarget(new targets.LambdaFunction(emptyFunction));
}
