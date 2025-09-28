import styles from "./AppLayout.module.css";

export function AppLayout() {
  return (
    <div className={styles.appLayout}>
      <header className={styles.topBar}>
        <h1 className={styles.title}>Choo Choo Clicker</h1>
        <div className={styles.resourceSummary}>
          <div className={styles.resourceItem}>
            <span className={styles.resourceLabel}>Momentum</span>
            <span className={styles.resourceValue}>0 / 10</span>
          </div>
          <div className={styles.resourceItem}>
            <span className={styles.resourceLabel}>Ressourcen</span>
            <span className={styles.resourceValue}>0</span>
          </div>
        </div>
      </header>
      <div className={styles.contentArea}>
        <main className={styles.mapArea}>
          <div className={styles.mapPlaceholder}>Kartenbereich</div>
        </main>
        <aside className={styles.controlPanel}>
          <section className={styles.panelSection}>
            <h2 className={styles.panelHeading}>Aktionen</h2>
            <button type="button" className={styles.actionButton}>
              Momentum kurbeln
            </button>
            <button type="button" className={styles.actionButton}>
              Gleis platzieren
            </button>
            <button type="button" className={styles.actionButton}>
              Gleis entfernen
            </button>
          </section>
          <section className={styles.panelSection}>
            <h2 className={styles.panelHeading}>Werkzeuge</h2>
            <ul className={styles.toolList}>
              <li>Gerade Strecke</li>
              <li>Kurve</li>
              <li>Kreuzung</li>
            </ul>
          </section>
        </aside>
      </div>
    </div>
  );
}
