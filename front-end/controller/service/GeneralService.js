export function writeToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        console.log("Copied: " + text)
    }).catch(err => {
        console.error("Fail to copy: " + err)
    })
}