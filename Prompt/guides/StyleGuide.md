# Style Guide: Informationsformatierung für LLMs

Dieser Leitfaden beschreibt Best Practices für die Speicherung, Strukturierung und Formatierung von Informationen, damit Large Language Models (LLMs) wie ChatGPT diese möglichst effizient nutzen können. Ziel ist es, Kontext effektiv verfügbar zu machen – nicht Prompt Engineering, sondern Datenorganisation.

---

## 1. Grundprinzipien

- **Kohärenz & Konsistenz**: Einheitliche Struktur und Namenskonventionen verwenden.
- **Semantische Klarheit**: Überschriften, Labels und Metadaten eindeutig halten.
- **Redundanz vermeiden**: Informationen nicht doppelt speichern, stattdessen referenzieren.
- **Granularisierung**: Große Texte in kleinere, in sich verständliche Chunks zerlegen.
- **Metadaten nutzen**: Quelle, Zeitstempel, Tags und Zusammenfassungen jedem Chunk hinzufügen.
- **Normierung**: Standardformate wie JSON, Markdown, YAML oder CSV einsetzen.
- **Versionierung**: Änderungen dokumentieren, alte Versionen archivieren.

---

## 2. Datenstruktur & Formate

### 2.1 Empfohlene Container
- **JSON-Lines**: Ein JSON pro Zeile, gut für Verarbeitung und Indexierung.
- **Markdown mit Frontmatter**: Lesbar und flexibel für Dokumente.
- **CSV / Parquet**: Für tabellarische Daten.
- **Graph / DB**: Für komplexe Entitäts-Beziehungs-Modelle.

### 2.2 Chunking & Segmentierung
- Chunks von 200–800 Tokens, je nach Modell.
- Überlappung 10–20 % zwischen Chunks.
- Jeder Chunk enthält Überschrift und Position im Dokument.

### 2.3 Metadaten pro Chunk
- `id`: eindeutiger Schlüssel  
- `source`: Dokumentname oder URL  
- `timestamp`: Erstellungs- oder Änderungszeit  
- `author`: Quelle / Autor  
- `tags`: Themenbegriffe  
- `language`: Sprachcode  
- `summary`: Kurzfassung  
- `chunk_index`, `parent_id`: Position / Zugehörigkeit  
- optional: `embedding_vector`, `confidence_score`

---

## 3. Beispielstruktur (JSON)

```json
{
  "id": "doc42_chunk_3",
  "parent_id": "doc42",
  "chunk_index": 3,
  "source": "https://beispiel.de/report.pdf",
  "timestamp": "2025-09-20T12:34:00Z",
  "author": "Musterautor",
  "language": "de",
  "tags": ["KI", "Retrieval", "Kontextmanagement"],
  "summary": "In diesem Abschnitt wird beschrieben, wie Daten in Chunks zerlegt werden.",
  "text": "Hier steht der eigentliche Textabschnitt …",
  "embedding_vector": [0.123, -0.456],
  "confidence_score": 0.87
}
```

---

## 4. Retrieval & Kontextnutzung

- **Embeddings**: Bei Indexierung generieren und speichern.  
- **Hybrid-Suche**: Kombination aus Embeddings und Schlüsselwortsuche.  
- **Reranking**: Ergebnisse nach Relevanz neu ordnen.  
- **Kompression**: Lange Texte zusätzlich in gekürzter Fassung speichern.  
- **Kontextmodule**: Prompt-Zusammenstellung in Sektionen (z. B. „Definitionen“, „Quellen“).

---

## 5. Pflege & Governance

- **Automatisierte Checks**: Fehlende Metadaten und Inkonsistenzen prüfen.  
- **Change-Log**: Änderungen dokumentieren.  
- **Feedback-Schleife**: Nutzungserfahrungen zur Optimierung einarbeiten.  
- **Datenschutz**: Sensible Infos maskieren oder einschränken.  
- **Dokumentation**: Style Guide versionieren und für alle Nutzer verfügbar halten.

---

## 6. Zusammenfassung

Effiziente Nutzung von Kontext in LLMs erfordert:  
- Klare Struktur, Chunking und Metadaten  
- Saubere Formate und Normierung  
- Retrieval-freundliche Vorbereitung  
- Kontinuierliche Pflege und Dokumentation

Dieser Guide dient als verbindliche Vorlage für die Speicherung und Aufbereitung von Daten für LLM-Kontexte.
