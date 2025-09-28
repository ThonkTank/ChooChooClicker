import React from "react";
import { act } from "react-dom/test-utils";
import { createRoot } from "react-dom/client";
import { describe, expect, it } from "vitest";
import App from "./App";

describe("App", () => {
  it("renders the primary layout panels", () => {
    const container = document.createElement("div");
    document.body.appendChild(container);

    const root = createRoot(container);

    act(() => {
      root.render(<App />);
    });

    expect(container.querySelector("header")).not.toBeNull();
    expect(container.querySelector("main")).not.toBeNull();
    expect(container.querySelector("aside")).not.toBeNull();

    act(() => {
      root.unmount();
    });
  });
});
