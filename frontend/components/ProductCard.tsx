import Link from 'next/link';
import Image from 'next/image';
import { Product } from '@/types';

interface ProductCardProps {
  product: Product;
}

export default function ProductCard({ product }: ProductCardProps) {
  const image = product.images[0] || '/placeholder-product.jpg';

  return (
    <Link
      href={`/products/${product.id}`}
      className="group bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-300"
    >
      <div className="relative aspect-square overflow-hidden bg-gray-200">
        <img
          src={image}
          alt={product.name}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
        />
        {product.stock === 0 && (
          <div className="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <span className="text-white font-semibold text-lg">Out of Stock</span>
          </div>
        )}
      </div>
      
      <div className="p-4">
        <h3 className="font-semibold text-lg text-gray-900 mb-1 truncate group-hover:text-indigo-600 transition">
          {product.name}
        </h3>
        
        <p className="text-sm text-gray-600 mb-2">{product.category}</p>
        
        <div className="flex items-center justify-between">
          <span className="text-xl font-bold text-indigo-600">
            ₹{product.price.toFixed(2)}
          </span>
          
          {product.stock > 0 && product.stock < 10 && (
            <span className="text-xs text-orange-600 font-medium">
              Only {product.stock} left
            </span>
          )}
        </div>
        
        {product.colors.length > 0 && (
          <div className="mt-3 flex gap-1">
            {product.colors.slice(0, 5).map((color, index) => (
              <div
                key={index}
                className="w-5 h-5 rounded-full border border-gray-300"
                style={{
                  backgroundColor: color.toLowerCase().replace(/\s/g, ''),
                }}
                title={color}
              />
            ))}
          </div>
        )}
      </div>
    </Link>
  );
}