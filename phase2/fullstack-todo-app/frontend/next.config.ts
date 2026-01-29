import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: "https://todo-app-api-jade.vercel.app/api/:path*",
      },
    ];
  },
};

export default nextConfig;
