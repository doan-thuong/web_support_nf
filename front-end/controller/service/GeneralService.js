export function writeToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        console.log("Copied: " + text)
    }).catch(err => {
        console.error("Fail to copy: " + err)
    })
}

export function generateUUID() {
    const firstChar = 'abcdef'
    const characters = '0123456789abcdef'
    let result = firstChar[Math.floor(Math.random() * firstChar.length)]
    for (let i = 1; i < 9; i++) {
        result += characters[Math.floor(Math.random() * characters.length)]
    }
    return result
}