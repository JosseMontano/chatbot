import { config } from "../config/config";

export async function fetchData(url: string) {
  try {
    const response = await fetch(config.endpoint + url);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error.message);
  }
}

export async function PostData(url: string, data: any) {
  try {
    let response = await fetch(config.endpoint + url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      // Manejar la respuesta exitosa aquí
      response = await response.json()
      const {data} = response as any
      return data;
    } else {
      // Manejar errores de respuesta aquí
      console.error("Error en la solicitud POST");
    }
  } catch (error) {
    // Manejar errores de red u otros errores aquí
    console.error("Error en la solicitud POST:", error);
  }
}
