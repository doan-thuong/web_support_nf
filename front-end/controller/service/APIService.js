export async function callAPI(url) {
    const configOptions = {
        method: "GET",
        headers: {
            "Content-Type": 'application/json'
        }
    }
    try {
        let data = await fetch(url, configOptions)

        if (!data.ok) {
            throw new Error(`Lỗi HTTP! Status: ${data.status} ${data.statusText}`);
        }

        const response = await data.json()

        return response
    } catch (error) {
        console.error('Lỗi khi gọi API:', error.message);
        throw error;
    }
}

export function cacheWhenReload(url) {
    const entries = performance.getEntriesByType("navigation")

    if (entries.length && entries[0].type === "reload") {
        let newUrl = new URL(url)
        newUrl.searchParams.set("cache", true)
        url = newUrl.toString()
    }

    return url
}

export function setParam(url, key, value) {
    let newUrl = new URL(url)

    newUrl.searchParams.set(key, value)

    return newUrl.toString()
}

export function deleteParam(url, key) {
    let newUrl = new URL(url)

    newUrl.searchParams.delete(key)

    return newUrl.toString()
}