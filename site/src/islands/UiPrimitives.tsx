/** @jsxImportSource solid-js */
import { createSignal, onCleanup, onMount, For, Show, createEffect } from 'solid-js';

// ─────────────────────────────────────────────────────────────────
// Select — accessible custom dropdown that matches the warm-paper
// theme. Replaces the native <select> which renders as the OS modal.
// ─────────────────────────────────────────────────────────────────

export interface SelectOption<T extends string> {
  value: T;
  label: string;
  hint?: string;
  disabled?: boolean;
}

export interface SelectProps<T extends string> {
  value: T;
  options: SelectOption<T>[];
  onChange: (value: T) => void;
  /** Tight (default) or wide; affects min-width of the trigger. */
  width?: 'auto' | 'wide';
  ariaLabel?: string;
}

export function Select<T extends string>(props: SelectProps<T>) {
  const [open, setOpen] = createSignal(false);
  const [highlight, setHighlight] = createSignal(0);
  let triggerEl: HTMLButtonElement | undefined;
  let panelEl: HTMLDivElement | undefined;

  const current = () => props.options.find((o) => o.value === props.value);

  function close() { setOpen(false); }

  function pick(value: T) {
    props.onChange(value);
    close();
    triggerEl?.focus();
  }

  function onKey(e: KeyboardEvent) {
    if (!open()) {
      if (['ArrowDown', 'ArrowUp', 'Enter', ' '].includes(e.key)) {
        e.preventDefault();
        const idx = Math.max(0, props.options.findIndex((o) => o.value === props.value));
        setHighlight(idx);
        setOpen(true);
      }
      return;
    }
    if (e.key === 'Escape') { e.preventDefault(); close(); return; }
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      let idx = highlight();
      do { idx = (idx + 1) % props.options.length; }
      while (props.options[idx].disabled && idx !== highlight());
      setHighlight(idx);
      return;
    }
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      let idx = highlight();
      do { idx = (idx - 1 + props.options.length) % props.options.length; }
      while (props.options[idx].disabled && idx !== highlight());
      setHighlight(idx);
      return;
    }
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      const o = props.options[highlight()];
      if (o && !o.disabled) pick(o.value);
      return;
    }
    if (e.key === 'Tab') close();
  }

  // close on outside click
  function onDocClick(e: MouseEvent) {
    if (!open()) return;
    const t = e.target as Node;
    if (panelEl?.contains(t) || triggerEl?.contains(t)) return;
    close();
  }
  onMount(() => document.addEventListener('mousedown', onDocClick));
  onCleanup(() => document.removeEventListener('mousedown', onDocClick));

  // Make sure the highlighted item is visible when navigating.
  createEffect(() => {
    if (!open() || !panelEl) return;
    const el = panelEl.querySelector(`[data-idx="${highlight()}"]`) as HTMLElement | null;
    el?.scrollIntoView({ block: 'nearest' });
  });

  return (
    <div class="relative inline-block">
      <button
        type="button"
        ref={(el) => (triggerEl = el)}
        aria-haspopup="listbox"
        aria-expanded={open() ? 'true' : 'false'}
        aria-label={props.ariaLabel}
        class={`inline-flex items-center justify-between gap-2 rounded-md border border-paper-300/80 dark:border-ink-600/60 bg-paper-50 dark:bg-nightbg-soft px-3 py-2 text-sm text-ink-700 dark:text-ink-50 hover:border-paper-400 dark:hover:border-ink-400/60 focus:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 dark:focus-visible:ring-accent-dark/40 transition-colors ${props.width === 'wide' ? 'min-w-[10rem]' : ''}`}
        onClick={() => setOpen(!open())}
        onKeyDown={onKey}
      >
        <span>{current()?.label ?? '—'}</span>
        <svg viewBox="0 0 16 16" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class={`text-ink-400 dark:text-ink-300 transition-transform ${open() ? 'rotate-180' : ''}`} aria-hidden="true">
          <path d="M3 6l5 5 5-5"/>
        </svg>
      </button>

      <Show when={open()}>
        <div
          ref={(el) => (panelEl = el)}
          role="listbox"
          aria-label={props.ariaLabel}
          class="absolute right-0 z-50 mt-1 min-w-[12rem] rounded-md border border-paper-300/80 dark:border-ink-600/60 bg-paper-50 dark:bg-nightbg-soft shadow-lg overflow-hidden"
          onKeyDown={onKey}
        >
          <ul class="py-1 max-h-80 overflow-auto">
            <For each={props.options}>
              {(opt, i) => {
                const active = () => opt.value === props.value;
                const hl = () => i() === highlight();
                return (
                  <li>
                    <button
                      type="button"
                      role="option"
                      aria-selected={active() ? 'true' : 'false'}
                      data-idx={i()}
                      disabled={opt.disabled}
                      class={`w-full flex items-center justify-between gap-3 px-3 py-1.5 text-sm text-left transition-colors ${
                        opt.disabled
                          ? 'text-ink-300 dark:text-ink-400 cursor-not-allowed'
                          : hl()
                            ? 'bg-accent/10 dark:bg-accent-dark/15 text-ink-700 dark:text-ink-50'
                            : active()
                              ? 'text-accent dark:text-accent-dark'
                              : 'text-ink-700 dark:text-ink-50 hover:bg-paper-200/60 dark:hover:bg-ink-700/40'
                      }`}
                      onMouseEnter={() => setHighlight(i())}
                      onClick={() => !opt.disabled && pick(opt.value)}
                    >
                      <span class="flex items-center gap-2">
                        <Show when={active()} fallback={<span class="w-3.5 inline-block" />}>
                          <svg viewBox="0 0 16 16" width="13" height="13" fill="currentColor" class="text-accent dark:text-accent-dark" aria-hidden="true"><path d="M13.5 4.5l-7 7-3-3 1-1 2 2 6-6z"/></svg>
                        </Show>
                        <span>{opt.label}</span>
                      </span>
                      <Show when={opt.hint}>
                        <span class="text-[11px] text-ink-400 dark:text-ink-300">{opt.hint}</span>
                      </Show>
                    </button>
                  </li>
                );
              }}
            </For>
          </ul>
        </div>
      </Show>
    </div>
  );
}

// ─────────────────────────────────────────────────────────────────
// Toggle — refined replacement for the native checkbox.
// ─────────────────────────────────────────────────────────────────

export interface ToggleProps {
  checked: boolean;
  onChange: (next: boolean) => void;
  label: string;
  hint?: string;
}

export function Toggle(props: ToggleProps) {
  return (
    <label class="flex items-start gap-2.5 cursor-pointer group">
      <button
        type="button"
        role="switch"
        aria-checked={props.checked ? 'true' : 'false'}
        class={`shrink-0 relative w-9 h-5 rounded-full transition-colors duration-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 dark:focus-visible:ring-accent-dark/40 ${
          props.checked
            ? 'bg-accent dark:bg-accent-dark'
            : 'bg-ink-200/60 dark:bg-ink-700/60'
        }`}
        onClick={() => props.onChange(!props.checked)}
      >
        <span
          class={`absolute top-0.5 left-0.5 w-4 h-4 rounded-full bg-paper-50 dark:bg-paper-50 shadow-sm transition-transform duration-200 ${
            props.checked ? 'translate-x-4' : 'translate-x-0'
          }`}
        />
      </button>
      <span class="text-sm leading-5 text-ink-600 dark:text-ink-100 group-hover:text-ink-700 dark:group-hover:text-ink-50 transition-colors">
        {props.label}
        <Show when={props.hint}>
          <span class="block text-[11px] text-ink-400 dark:text-ink-300 mt-0.5">{props.hint}</span>
        </Show>
      </span>
    </label>
  );
}
