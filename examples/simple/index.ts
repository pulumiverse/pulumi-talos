import * as talos from "@pulumi/talos";

const random = new talos.Random("my-random", { length: 24 });

export const output = random.result;
