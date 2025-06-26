Thales Safenet Log Parser for Sekoia.IO

This project provides a custom log parser designed to normalize and adapt **Thales Safenet** logs for seamless integration with the **Sekoia.IO SIEM** platform.

## 🛠️ Features

- Parses Thales Safenet logs with specific formatting and structure.
- Transforms and enriches raw log entries into a structured JSON format compatible with Sekoia.IO.
- Easily extensible for additional log types or normalization rules.

1. Input: Raw log file or stream from Thales Safenet.
2. Processing: The script applies parsing rules and structure transformation.
3. Output: JSON-formatted logs ready for ingestion by Sekoia.IO (via log forwarder or API).
