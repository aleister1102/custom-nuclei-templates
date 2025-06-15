# Technology Prometheus Templates

## Summary
- **Total templates**: 17
- **Category**: technology-prometheus

## Templates List

### Medium Severity (2 templates)

#### Prometheus  - Open Redirect
- **File**: `CVE-2021-29622.yaml`
- **Author**: geeknik
- **Tags**: cve,cve2021,prometheus,redirect
- **Description**: Prometheus 2.23.0 through 2.26.0 and 2.27.0 contains an open redirect vulnerability. To ensure a seamless transition to 2.27.0, the default UI was changed to the new UI with a URL prefixed by /new red...

#### Prometheus Metrics - Detect
- **File**: `prometheus-metrics_1.yaml`
- **Author**: dhiyaneshDK,philippedelteil
- **Tags**: exposure,prometheus,hackerone,config
- **Description**: Prometheus metrics page was detected.

### Low Severity (6 templates)

#### Exposed Prometheus
- **File**: `exposed-prometheus-log.yaml`
- **Author**: dhiyaneshDK
- **Tags**: exposure,prometheus,logs
- **Description**: No description

#### Prometheus.io exposed panel
- **File**: `prometheus-exposed-panel.yaml`
- **Author**: organiccrap
- **Tags**: panel,prometheus
- **Description**: No description

#### Exposed Prometheus
- **File**: `prometheus-log.yaml`
- **Author**: dhiyaneshDK
- **Tags**: prometheus
- **Description**: No description

#### Exposed Prometheus metrics
- **File**: `prometheus-metrics.yaml`
- **Author**: dhiyaneshDK, philippedelteil
- **Tags**: config,exposure,prometheus
- **Description**: No description

#### Prometheus.io exposed panel
- **File**: `promothoues-panel.yaml`
- **Author**: organiccrap
- **Tags**: 
- **Description**: No description

#### Exposed Prometheus
- **File**: `prometheus-log_1.yaml`
- **Author**: dhiyaneshDK
- **Tags**: prometheus
- **Description**: No description

### Info Severity (9 templates)

#### Prometheus config API endpoint
- **File**: `prometheus-config-endpoint.yaml`
- **Author**: geeknik
- **Tags**: prometheus,exposure
- **Description**: The config endpoint returns the loaded Prometheus configuration file. This file also contains addresses of targets and alerting/discovery services alongside the credentials required to access them. Us...

#### Prometheus Config API Endpoint Discovery
- **File**: `prometheus-config.yaml`
- **Author**: geeknik
- **Tags**: prometheus,config
- **Description**: A Prometheus config API endpoint was discovered. The config endpoint returns the loaded Prometheus configuration file along with the addresses of targets and alerting/discovery services alongside the ...

#### Prometheus flags API endpoint
- **File**: `prometheus-flags-endpoint.yaml`
- **Author**: geeknik
- **Tags**: prometheus,exposure
- **Description**: The flags endpoint provides a full path to the configuration file. If the file is stored in the home directory, it may leak a username.

#### Prometheus flags API endpoint
- **File**: `prometheus-flags.yaml`
- **Author**: geeknik
- **Tags**: prometheus,leak
- **Description**: The flags endpoint provides a full path to the configuration file. If the file is stored in the home directory, it may leak a username.

#### Prometheus config API endpoint
- **File**: `prometheus-config_1.yaml`
- **Author**: geeknik
- **Tags**: prometheus,config
- **Description**: The config endpoint returns the loaded Prometheus configuration file. This file also contains addresses of targets and alerting/discovery services alongside the credentials required to access them. Us...

#### Prometheus exporter detect
- **File**: `prometheus-exporter.yaml`
- **Author**: jarijaas
- **Tags**: prometheus
- **Description**: Prometheus exporter detector

#### Prometheus flags API endpoint
- **File**: `prometheus-flags_1.yaml`
- **Author**: geeknik
- **Tags**: prometheus,leak
- **Description**: The flags endpoint provides a full path to the configuration file. If the file is stored in the home directory, it may leak a username.

#### Prometheus Panel - Detect
- **File**: `prometheus-exposed-panel_1.yaml`
- **Author**: organiccrap
- **Tags**: panel,prometheus
- **Description**: Prometheus panel was detected.

#### Prometheus Pushgateway Panel - Detect
- **File**: `prometheus-pushgateway-exposed-panel.yaml`
- **Author**: codexlynx
- **Tags**: panel,prometheus,pushgateway
- **Description**: Prometheus Pushgateway panel was detected.

