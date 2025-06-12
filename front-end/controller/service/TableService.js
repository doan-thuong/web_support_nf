import { status } from "../config/StatusConfig.js"

export function getStatus() {
    return Object.keys(status)
}