import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_article(url):
    """
    This function connects to a Wikipedia URL, extracts the main title, 
    and gathers all long paragraphs for a professional text output.
    """
    # Using a real browser User-Agent to avoid being blocked by servers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    
    try:
        # Sending a GET request to the server
        response = requests.get(url, headers=headers)
        
        # Professional Check: verify if the request was successful (Status 200 OK)
        if response.status_code == 200:
            print(f"✅ Connection successful! Status Code: {response.status_code}")
        else:
            print(f"❌ Connection failed. Status: {response.status_code}")
            return None
            
        # Parsing the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        extracted_data = []

        # Iterating through headings and paragraphs to maintain document structure
        for element in soup.find_all(['h1', 'h2', 'h3', 'p']):
            text = element.text.strip()
            
            # Filtering out short strings to get only meaningful content
            if len(text) > 45: 
                if element.name.startswith('h'):
                    # Formatting headings for better readability
                    extracted_data.append(f"\n{'='*5} {text.upper()} {'='*5}\n")
                else:
                    extracted_data.append(text)

        return extracted_data

    except Exception as e:
        print(f"❌ An error occurred during scraping: {e}")
        return None

# --- Main Execution ---
if __name__ == "__main__":
    # Target: Python Programming Language article on English Wikipedia
    target_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    
    print("🌐 Initializing scraper, please wait...")
    results = scrape_wikipedia_article(target_url)

    if results:
        # Saving the output with UTF-8-SIG to support all characters
        # Note: This path is designed for mobile Pydroid 3 users
        output_file = "/storage/emulated/0/Download/python_wiki_results.txt"
        
        try:
            with open(output_file, "w", encoding="utf-8-sig") as f:
                f.write(f"PROJECT: WIKIPEDIA CONTENT EXTRACTOR\n")
                f.write(f"SOURCE URL: {target_url}\n")
                f.write("-" * 50 + "\n")
                for line in results:
                    f.write(line + "\n\n")
            print(f"✅ Success! File saved to: {output_file}")
        except Exception as file_error:
            print(f"❌ Could not save file: {file_error}")
    else:
        print("❌ No data was extracted.")

