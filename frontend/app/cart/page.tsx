'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { cartAPI } from '@/lib/api';
import { CartItem } from '@/types';
import { Trash2, Plus, Minus, ShoppingBag } from 'lucide-react';
import Link from 'next/link';

export default function CartPage() {
  const router = useRouter();
  const [cartItems, setCartItems] = useState<CartItem[]>([]);
  const [totals, setTotals] = useState({ subtotal: 0, tax: 0, total: 0 });

  useEffect(() => {
    loadCart();
  }, []);

  const loadCart = () => {
    const items = cartAPI.getCart();
    setCartItems(items);
    setTotals(cartAPI.getCartTotal());
  };

  const updateQuantity = (index: number, newQuantity: number) => {
    cartAPI.updateQuantity(index, newQuantity);
    loadCart();
    window.dispatchEvent(new Event('cartUpdated'));
  };

  const removeItem = (index: number) => {
    if (confirm('Remove this item from cart?')) {
      cartAPI.removeItem(index);
      loadCart();
      window.dispatchEvent(new Event('cartUpdated'));
    }
  };

  if (cartItems.length === 0) {
    return (
      <div className="container mx-auto px-4 py-16 text-center">
        <ShoppingBag className="w-24 h-24 mx-auto text-gray-400 mb-4" />
        <h1 className="text-3xl font-bold mb-4">Your cart is empty</h1>
        <p className="text-gray-600 mb-8">Add some products to get started!</p>
        <Link
          href="/products"
          className="inline-block px-8 py-3 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 transition"
        >
          Shop Now
        </Link>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Shopping Cart</h1>

      <div className="grid lg:grid-cols-3 gap-8">
        {/* Cart Items */}
        <div className="lg:col-span-2 space-y-4">
          {cartItems.map((item, index) => (
            <div key={index} className="bg-white rounded-lg shadow p-4 flex gap-4">
              <img
                src={item.product.images[0] || '/placeholder-product.jpg'}
                alt={item.product.name}
                className="w-24 h-24 object-cover rounded"
              />
              
              <div className="flex-1">
                <Link
                  href={`/products/${item.product.id}`}
                  className="font-semibold text-lg hover:text-indigo-600 transition"
                >
                  {item.product.name}
                </Link>
                <p className="text-gray-600 text-sm">{item.product.category}</p>
                {item.selected_size && (
                  <p className="text-sm text-gray-600">Size: {item.selected_size}</p>
                )}
                {item.selected_color && (
                  <p className="text-sm text-gray-600">Color: {item.selected_color}</p>
                )}
                <p className="text-indigo-600 font-semibold mt-2">
                  ₹{item.product.price.toFixed(2)}
                </p>
              </div>

              <div className="flex flex-col items-end justify-between">
                <button
                  onClick={() => removeItem(index)}
                  className="text-red-600 hover:text-red-700 p-2"
                >
                  <Trash2 className="w-5 h-5" />
                </button>

                <div className="flex items-center gap-2">
                  <button
                    onClick={() => updateQuantity(index, item.quantity - 1)}
                    className="p-1 border border-gray-300 rounded hover:bg-gray-50"
                  >
                    <Minus className="w-4 h-4" />
                  </button>
                  <span className="w-8 text-center font-semibold">{item.quantity}</span>
                  <button
                    onClick={() => updateQuantity(index, item.quantity + 1)}
                    className="p-1 border border-gray-300 rounded hover:bg-gray-50"
                    disabled={item.quantity >= item.product.stock}
                  >
                    <Plus className="w-4 h-4" />
                  </button>
                </div>

                <p className="font-bold text-lg">
                  ₹{(item.product.price * item.quantity).toFixed(2)}
                </p>
              </div>
            </div>
          ))}
        </div>

        {/* Order Summary */}
        <div className="lg:col-span-1">
          <div className="bg-white rounded-lg shadow p-6 sticky top-20">
            <h2 className="text-xl font-bold mb-4">Order Summary</h2>
            
            <div className="space-y-2 mb-4">
              <div className="flex justify-between">
                <span className="text-gray-600">Subtotal</span>
                <span className="font-semibold">₹{totals.subtotal.toFixed(2)}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Tax (18%)</span>
                <span className="font-semibold">₹{totals.tax.toFixed(2)}</span>
              </div>
              <div className="border-t pt-2 flex justify-between text-lg">
                <span className="font-bold">Total</span>
                <span className="font-bold text-indigo-600">₹{totals.total.toFixed(2)}</span>
              </div>
            </div>

            <button
              onClick={() => router.push('/checkout')}
              className="w-full py-3 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 transition"
            >
              Proceed to Checkout
            </button>

            <Link
              href="/products"
              className="block text-center mt-4 text-indigo-600 hover:underline"
            >
              Continue Shopping
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}