import type { Config } from "tailwindcss";

// Tailwind configuration
// - Scans the Next.js app directory and components
// - Provides a simple brand color placeholder
const config: Config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./lib/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: "hsl(var(--brand) / <alpha-value>)",
      },
    },
  },
  plugins: [],
};

export default config;


