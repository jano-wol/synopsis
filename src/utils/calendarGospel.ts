import type { GospelScheme, QuoteScheme } from "@/interfaces/dailyGospelInterface";

export async function fetchGospel(date: Date): Promise<GospelScheme> {
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        try {
          const response = await fetch(`https://www.synopticus.org/gospel-calendar/api.php?date=${date.getFullYear()}-${month}-${day}`);
          if (!response.ok) {
            throw new Error(`Error: ${response.status} - ${response.statusText}`);
          }
          const data = await response.json();
          return {color: data.colors ? data.colors[0] : null, gospel: data.gospels[0]};
        }
        catch (error) {
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