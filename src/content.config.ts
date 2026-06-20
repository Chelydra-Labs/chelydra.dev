import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    tagline: z.string(),
    description: z.string(),
    repo: z.string(),
    homepage: z.string().url().optional(),
    docs: z.string().url().optional(),
    license: z.string().optional(),
    language: z.string().optional(),
    order: z.number().default(0),
    featured: z.boolean().default(true),
    accent: z.string().optional(),
    logo: z.string().optional(),
    published: z.coerce.date().optional(),
  }),
});

export const collections = { projects };
