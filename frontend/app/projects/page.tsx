// Projects page
// - Upload/create projects and list existing ones
"use client";
import { useEffect, useState } from "react";
import { listProjects } from "../api/projects";

type Project = { id: string; name: string };

export default function ProjectsPage() {
  const [projects, setProjects] = useState<Project[]>([]);

  useEffect(() => {
    listProjects().then(setProjects).catch(() => setProjects([]));
  }, []);

  return (
    <section className="container py-8">
      <h2 className="text-2xl font-semibold">Projects</h2>
      <p className="mt-2 text-gray-600">Create or upload new models.</p>

      <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {projects.map((p) => (
          <div key={p.id} className="rounded-lg border bg-white p-4">
            <h3 className="font-medium">{p.name}</h3>
            <p className="text-sm text-gray-500">Project ID: {p.id}</p>
          </div>
        ))}
        {projects.length === 0 && (
          <div className="rounded-lg border bg-white p-4 text-gray-500">
            No projects yet.
          </div>
        )}
      </div>
    </section>
  );
}


