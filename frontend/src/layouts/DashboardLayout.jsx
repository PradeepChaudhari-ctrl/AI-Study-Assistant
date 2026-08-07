import { Link, Outlet, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function DashboardLayout() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  function handleLogout() {
    logout();
    navigate("/login");
  }

  return (
    <div className="flex min-h-screen">
      <aside className="w-64 bg-slate-900 text-white p-6">
        <h1 className="text-2xl font-bold mb-8">
          AI Study Assistant 🚀
        </h1>

        <nav className="space-y-4">
          <Link className="block hover:text-blue-400" to="/dashboard">
            Dashboard
          </Link>

          <Link className="block hover:text-blue-400" to="/dashboard/upload">
            Upload PDF
          </Link>

          <Link className="block hover:text-blue-400" to="/dashboard/documents">
            Documents
          </Link>

          <button
            onClick={handleLogout}
            className="mt-10 rounded-lg bg-red-600 px-4 py-2 hover:bg-red-700"
          >
            Logout
          </button>
        </nav>
      </aside>

      <main className="flex-1 bg-slate-100 p-8">
        <Outlet />
      </main>
    </div>
  );
}