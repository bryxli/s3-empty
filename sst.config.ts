import { SSTConfig } from "sst";
import { LambdaStack } from "./stacks/LambdaStack";

export default {
  config(_input) {
    return {
      name: "s3-empty",
      region: "us-east-1",
    };
  },
  stacks(app) {
    app.stack(LambdaStack);
  }
} satisfies SSTConfig;
