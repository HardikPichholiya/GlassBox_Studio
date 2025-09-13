// Dashboard page
// - Placeholder for key charts and recent activity
import dynamic from "next/dynamic";

const Plot = dynamic(() => import("react-plotly.js"), { ssr: false });

export default function DashboardPage() {
  return (
    <section className="container py-8">
      <h2 className="text-2xl font-semibold">Dashboard</h2>
      <p className="mt-2 text-gray-600">Recent metrics and model health.</p>

      <div className="mt-6 rounded-lg border bg-white p-4">
        <Plot
          data={[
            { x: ["A", "B", "C"], y: [20, 14, 23], type: "bar" },
          ]}
          layout={{ title: "Example Bar Chart", autosize: true }}
          style={{ width: "100%", height: 360 }}
          config={{ displayModeBar: false }}
        />
      </div>
    </section>
  );
}


