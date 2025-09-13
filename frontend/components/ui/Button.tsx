// Button: Simple reusable button component
import { ButtonHTMLAttributes } from "react";
import clsx from "clsx";

type Props = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "secondary";
};

export function Button({ variant = "primary", className, ...props }: Props) {
  return (
    <button
      className={clsx(
        "inline-flex items-center justify-center rounded-md px-4 py-2 text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2",
        variant === "primary"
          ? "bg-gray-900 text-white hover:bg-gray-800 focus:ring-gray-900"
          : "border border-gray-300 bg-white text-gray-900 hover:bg-gray-50 focus:ring-gray-300",
        className
      )}
      {...props}
    />
  );
}


