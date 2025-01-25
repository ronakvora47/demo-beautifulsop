import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.shortcuts import render

def scrape_titles(request):
    print('View is being triggered')  # Check if the view is accessed
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print('AJAX request detected')  # Confirm AJAX request

        # URL to scrape
        url = "https://www.amazon.in/"
        print(f'Scraping URL: {url}')

        try:
            # Make an HTTP request to the URL
            response = requests.get(url)
            print(f'HTTP Response Status: {response.status_code}')

            if response.status_code == 200:
                print('Page successfully fetched')
                
                # Parse the HTML content
                soup = BeautifulSoup(response.content, 'lxml')

                # Extract titles (example: `<h1>` tags)
                titles = [title.get_text(strip=True) for title in soup.find_all('')]

                print('Scraped Titles:', titles)
                return JsonResponse({'titles': titles})
            else:
                print('Failed to fetch the page')
                return JsonResponse({'error': 'Failed to fetch the page'}, status=500)
        except Exception as e:
            print('An error occurred:', e)
            return JsonResponse({'error': str(e)}, status=500)
    else:
        print('Non-AJAX request or incorrect method')
        return render(request, 'scrape_titles.html')
