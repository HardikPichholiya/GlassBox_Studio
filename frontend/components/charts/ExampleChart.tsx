// ExampleChart: Demonstrates Plotly usage in a component
import dynamic from "next/dynamic";

const Plot = dynamic(() => import("react-plotly.js"), { ssr: false });

export function ExampleChart() {
  return (
    <Plot
      data={[{ x: [1, 2, 3], y: [2, 6, 3], type: "scatter", mode: "lines+markers" }]}
      layout={{ title: "Example Line Chart", autosize: true }}
      style={{ width: "100%", height: 320 }}
      config={{ displayModeBar: false }}
    />
  );
}


