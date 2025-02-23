import type { GospelScheme, QuoteScheme } from "@/interfaces/dailyGospelInterface";

export async function fetchGospel(date: Date): Promise<QuoteScheme> {
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const url = `${import.meta.env.BASE_URL}calendar/${date.getFullYear()}/${month}/${day}.json`;
        const response = await fetch(url);
        const data = await response.json();
        return data.daily_gospel[0];
}

export function isValidDate(value : string) : boolean {
  const regex = /^\d{4}-\d{2}-\d{2}$/;

  if (!regex.test(value)) {
      return false;
  }

  return true;
}