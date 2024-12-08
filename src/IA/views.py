from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

def call_ai_api(request):
    # Clé API et URL de l'API
    api_key = settings.API_KEY
    api_url = (
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    )

    # Corps de la requête
    data = {
        "contents": [
            {
                "parts": [
                    {"text": "Explain how AI works"}
                ]
            }
        ]
    }

    # Headers de la requête
    headers = {
        "Content-Type": "application/json",
    }

    # Envoi de la requête
    try:
        response = requests.post(f"{api_url}?key={api_key}", json=data, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        # Extraire le texte généré
        generated_text = response_data["candidates"][0]["content"]["parts"][0]["text"]

        # Retourner le texte généré dans une réponse JSON
        return JsonResponse({"generated_text": generated_text}, safe=False)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": "API request failed", "details": str(e)}, status=500)


def ai_prompt(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")  # Récupérer le prompt envoyé depuis le frontend
        
        # URL de l'API et clé API
        api_key = settings.API_KEY
        api_url = (
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
        )
        
        # Corps de la requête
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }
        
        headers = {"Content-Type": "application/json"}

        try:
            # Appel API
            response = requests.post(f"{api_url}?key={api_key}", json=data, headers=headers)
            response.raise_for_status()
            response_data = response.json()

            # Extraire le texte généré
            generated_text = response_data["candidates"][0]["content"]["parts"][0]["text"]

            return JsonResponse({"response": generated_text})

        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": "API request failed", "details": str(e)}, status=500)
    
    return render(request, "ai_prompt.html")  # Retourne la page HTML pour le formulaire
