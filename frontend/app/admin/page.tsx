'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/lib/auth-context';
import Link from 'next/link';
import { Package, ShoppingBag, Users } from 'lucide-react';

export default function AdminPage() {
  const { user } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!user) {
      router.push('/auth/login');
    } else if (!user.is_admin) {
      router.push('/');
    }
  }, [user]);

  if (!user || !user.is_admin) {
    return <div className="container mx-auto px-4 py-8">Loading...</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Admin Dashboard</h1>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Link
          href="/admin/products"
          className="block bg-white rounded-lg shadow p-6 hover:shadow-lg transition"
        >
          <div className="flex items-center gap-4 mb-4">
            <div className="p-3 bg-indigo-100 rounded-lg">
              <ShoppingBag className="w-8 h-8 text-indigo-600" />
            </div>
            <h2 className="text-xl font-bold">Products</h2>
          </div>
          <p className="text-gray-600">Manage your product catalog</p>
        </Link>

        <Link
          href="/admin/orders"
          className="block bg-white rounded-lg shadow p-6 hover:shadow-lg transition"
        >
          <div className="flex items-center gap-4 mb-4">
            <div className="p-3 bg-green-100 rounded-lg">
              <Package className="w-8 h-8 text-green-600" />
            </div>
            <h2 className="text-xl font-bold">Orders</h2>
          </div>
          <p className="text-gray-600">View and manage customer orders</p>
        </Link>

        <div className="block bg-white rounded-lg shadow p-6 opacity-50 cursor-not-allowed">
          <div className="flex items-center gap-4 mb-4">
            <div className="p-3 bg-purple-100 rounded-lg">
              <Users className="w-8 h-8 text-purple-600" />
            </div>
            <h2 className="text-xl font-bold">Customers</h2>
          </div>
          <p className="text-gray-600">Coming soon...</p>
        </div>
      </div>
    </div>
  );
}