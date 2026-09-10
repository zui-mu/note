// Node-RED Function 节点：将 Outputs 设置为 4。
// 输出顺序固定为：温度、湿度、声音、光线。
let data;

try {
    // MQTT in 的 payload 可能是 Buffer、JSON 字符串或已经解析好的对象。
    if (Buffer.isBuffer(msg.payload)) {
        data = JSON.parse(msg.payload.toString());
    } else if (typeof msg.payload === "string") {
        data = JSON.parse(msg.payload);
    } else if (msg.payload !== null && typeof msg.payload === "object") {
        data = msg.payload;
    } else {
        throw new Error("输入不是有效 JSON 数据");
    }

    const keys = ["temperature", "humidity", "sound", "light"];

    for (const key of keys) {
        if (!Object.prototype.hasOwnProperty.call(data, key)) {
            throw new Error("缺少字段：" + key);
        }

        if (typeof data[key] !== "number" || !Number.isFinite(data[key])) {
            throw new Error(key + "不是有效数值");
        }
    }

    return [
        { payload: data.temperature, topic: "温度" },
        { payload: data.humidity, topic: "湿度" },
        { payload: data.sound, topic: "声音" },
        { payload: data.light, topic: "光线" },
    ];
} catch (error) {
    node.warn("环境数据解析失败：" + error.message);

    // 对应的 Dashboard 节点不会收到错误格式的数据。
    return [null, null, null, null];
}
