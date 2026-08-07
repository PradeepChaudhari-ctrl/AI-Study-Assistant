import { forwardRef } from "react";

const Input = forwardRef(function Input(
  { label, ...props },
  ref
) {
  return (
    <div className="mb-4">
      <label className="mb-2 block text-sm font-medium text-slate-700">
        {label}
      </label>

      <input
        ref={ref}
        {...props}
        className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-200"
      />
    </div>
  );
});

export default Input;