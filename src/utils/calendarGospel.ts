import type { GospelScheme, QuoteScheme } from "@/interfaces/dailyGospelInterface";

export async function fetchGospel(date: Date): Promise<GospelScheme> {
    try {
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        // const response = await fetch(`http://localhost:3000/${date.getFullYear()}/${month}/${day}`);
        const response = await fetch(`https://igenaptar-api-production.up.railway.app/${date.getFullYear()}/${month}/${day}`);
        if (!response.ok) {
          throw new Error(`Error: ${response.status} - ${response.statusText}`);
        }
        
        const data = await response.json();
        return data;

    } catch (error) {
        console.error("Fetch error:", error);
        throw error;
    }
}

export function isValidDate(value : string) : boolean {
  const regex = /^\d{4}-\d{2}-\d{2}$/;

  if (!regex.test(value)) {
      return false;
  }

  return true;
}