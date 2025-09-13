// Home page
// - Landing surface that links to dashboard and projects
import Link from "next/link";

export default function HomePage() {
  return (
    <main className="container py-12">
      <h1 className="text-3xl font-semibold">Glassbox AI Studio</h1>
      <p className="mt-2 text-gray-600">
        Evaluate, audit, and explain your machine learning models.
      </p>

      <div className="mt-8 flex gap-4">
        <Link
          href="/dashboard"
          className="rounded-md bg-gray-900 px-4 py-2 text-white hover:bg-gray-800"
        >
          Go to Dashboard
        </Link>
        <Link
          href="/projects"
          className="rounded-md border px-4 py-2 hover:bg-gray-100"
        >
          Manage Projects
        </Link>
      </div>
    </main>
  );
}


