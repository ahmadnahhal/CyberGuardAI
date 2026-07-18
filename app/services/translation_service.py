TRANSLATIONS = {
    "incident_created": {
        "english": "✅ Incident created successfully.",
        "french": "✅ Incident créé avec succès.",
    },
    "report_created": {
        "english": "📄 Report generated successfully.",
        "french": "📄 Rapport généré avec succès.",
    },
    "operation_cancelled": {
        "english": "Operation cancelled.",
        "french": "Opération annulée.",
    },
    "yes_no": {
        "english": "Please answer Yes or No.",
        "french": "Veuillez répondre par Oui ou Non.",
    },
    "memory_saved": {
        "english": "Memory saved.",
        "french": "Mémoire enregistrée.",
    },
}


def tr(key: str, language: str):

    return TRANSLATIONS.get(
        key,
        {},
    ).get(
        language,
        TRANSLATIONS[key]["english"],
    )