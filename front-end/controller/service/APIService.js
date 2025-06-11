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