// Root layout for the Next.js App Router
// - Imports global Tailwind styles
// - Defines metadata and the base HTML structure

import "../styles/globals.css";
import type { ReactNode } from "react";

export const metadata = {
  title: "Glassbox AI Studio",
  description: "Evaluate, audit, and explain ML models.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" className="h-full bg-gray-50">
      <body className="min-h-screen text-gray-900 antialiased">
        {/* App-wide layout: header/sidebar can be added here later */}
        {children}
      </body>
    </html>
  );
}


