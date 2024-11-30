import type { DailyGospelScheme, QuoteScheme } from "@/interfaces/dailyGospelInterface";

export async function fetchGospel(date: Date): Promise<DailyGospelScheme> {
    try {
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const response = await fetch(`https://igenaptar-api-production.up.railway.app/fetch-webpage/${date.getFullYear()}/${month}/${day}`);
        
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

export function parseCitation(citation: string) : QuoteScheme {
  const regex = /^([A-Za-z]{2})\s(\d+),(\d+[ab]?)(?:-(\d+[ab]?)(?:,(\d+[ab]?))?)?/;
  const match = citation.match(regex);

  if (match) {
    return {
      evangelist: match[1].toLowerCase(),
      start: {
        chapter: match[2],
        verse: match[3],
      },
      end: {
        chapter: match[5] ? match[4] : match[2],
        verse: match[5] || (match[4] || match[3]),
      }
    };
  } else {
    throw new Error('Invalid reference format');
  }
}

export function isValidDate(value : string) : boolean {
  const regex = /^\d{4}-\d{2}-\d{2}$/;

  if (!regex.test(value)) {
      return false;
  }

  return true;
}