
#include <stdio.h>
#include "../inc/im_incs.h"

namespace im {
////////////////////////////////////////////////////////////////////////////////////////////////////
using namespace bs;

void grayimage::tobw(t_pixel valve) throwempty
{
	for(t_pixel *p = begin(), *q = end(); p < q; ++p)
		*p = *p >= valve ? PIX_WHITE : PIX_BLACK;
	return;
}

void grayimage::crop(_rect range, grayimage &img) const throwempty
{
	range.assign(range.left, range.top, range.right, range.base);

	img.create(range.height(), range.width());

	for(t_i32 i = range.top; i < range.base; ++i)
		for(t_i32 j = range.left; j < range.right; ++j)
			if(0 <= i && i < height() && 0 <= j && j < width())
				img[i - range.top][j - range.left] = pixel(i, j);
	return;
}

void grayimage::crop33(t_i32 y, t_i32 x, t_pixel a[3][3]) const throwempty
{
	for(t_i32 i = -1; i < 2; ++i)
		for(t_i32 j = -1; j < 2; ++j)
			if(0 <= y + i && y + i < height() && 0 <= x + j && x + j < width())
				a[1 + i][1 + j] = pixel(y + i, x + j);
	return;
}

////////////////////////////////////////////////////////////////////////////////////////////////////

void grayimage::bw_thin2() throw(exception)
{
	const t_i32 height = this->height();
	const t_i32 width = this->width();

	t_pixel a[3][3];

	grayimage front(height, width);

	t_bool run = b_true;
	while(run)
	{
		run = b_false;
		algorithms::sets(front.begin(), front.end(), PIX_WHITE);

		for(t_i32 i = 0; i < height; ++i)
			for(t_i32 j = 0; j < width; ++j)
			{
				if(IS_WHITE(pixel(i, j)))
					continue;

				operators::opt33_sets(a, PIX_WHITE);
				crop33(i, j, a);

				if(1 != operators::bw33_connect_degree(a))
				{
					front.pixel(i, j) = PIX_BLACK;
					continue;
				}

				if(1 == operators::bw33_connect_degree(a)
					&& 2 == operators::bw33_blacks(a))
				{
					front.pixel(i, j) = PIX_BLACK;
					continue;
				}

				if(IS_BLACK(a[0][1]) && IS_BLACK(a[1][0]))
				{
					front.pixel(i, j) = PIX_BLACK;
					continue;
				}
				else
				{
					front.pixel(i, j) = PIX_WHITE;
					run = b_true;
				}
			}

		assign(front);
	}

	run = b_true;
	while(run)
	{
		run = b_false;
		algorithms::sets(front.begin(), front.end(), PIX_WHITE);

		for(t_i32 i = 0; i < height; ++i)
			for(t_i32 j = 0; j < width; ++j)
			{
				if(IS_WHITE(pixel(i, j)))
					continue;

				operators::opt33_sets(a, PIX_WHITE);
				crop33(i, j, a);

				if(1 != operators::bw33_connect_degree(a))
				{
					front.pixel(i, j) = PIX_BLACK;
					continue;
				}

				if(1 == operators::bw33_connect_degree(a)
					&& 2 == operators::bw33_blacks(a))
				{
					front.pixel(i, j) = PIX_BLACK;
					continue;
				}

				if(IS_BLACK(a[2][1]) && IS_BLACK(a[2][1]))
				{
					front.pixel(i, j) = PIX_BLACK;
					continue;
				}
				else
				{
					front.pixel(i, j) = PIX_WHITE;
					run = b_true;
				}
			}

		assign(front);
	}

	return;
}

void grayimage::bw_thin() throw(exception)
{
	t_i32 height = this->height();
	t_i32 width = this->width();

	grayimage front(height, width);

	t_pixel a[3][3], b[3][3];

	t_bool run = b_true;
	while(run)
	{
		run = b_false;

		algorithms::sets(front.begin(), front.end(), PIX_WHITE);

		for(t_i32 i = 0; i < height; ++i)
			for(t_i32 j = 0; j < width; ++j)
			{
				if(IS_WHITE(pixel(i, j)))
					continue;

				memset(a[0], PIX_WHITE, sizeof(a));
				crop33(i, j, a);

				t_i32 count = operators::bw33_blacks(a) - 1;
				if(count < 2 || count > 6)
				{
					front.pixel(i, j) = PIX_BLACK;
					continue;
				}

				if(operators::bw33_connect_degree(a) != 1)
				{
					front.pixel(i, j) = PIX_BLACK;
					continue;
				}

				if(IS_BLACK(a[0][1]) && IS_BLACK(a[1][0]) && IS_BLACK(a[1][2]))
				{
					memset(b[0], PIX_WHITE, sizeof(b));
					crop33(i - 1, j, b);

					if(operators::bw33_connect_degree(b) == 1)
					{
						front.pixel(i, j) = PIX_BLACK;
						continue;
					}
				}

				if(IS_BLACK(a[0][1]) && IS_BLACK(a[1][0]) && IS_BLACK(a[2][1]))
				{
					memset(b[0], PIX_WHITE, sizeof(b));
					crop33(i, j - 1, b);
					
					if(operators::bw33_connect_degree(b) == 1)
					{
						front.pixel(i, j) = PIX_BLACK;
						continue;
					}
				}

				front.pixel(i, j) = PIX_WHITE;
				run = b_true;
			}

		assign(front);
	}

	assign(front);

	return;
}

void grayimage::bw_getrange(_rect &range) throwempty
{
	t_i32 i = 0;
	for(i = 0; i < height(); ++i)
		if(bw_row_blacks(i) > 0)
			break;
	range.top = i;

	for(i = height() - 1; i >= 0; --i)
		if(bw_row_blacks(i) > 0)
			break;
	range.base = i + 1;

	for(i = 0; i < width(); ++i)
		if(bw_col_blacks(i) > 0)
			break;
	range.left = i;

	for(i = width() - 1; i >= 0; --i)
		if(bw_col_blacks(i) > 0)
			break;
	range.right = i + 1;

	return;
}

t_i32 grayimage::bw_row_blacks(t_i32 row) const throwempty
{
	if(row < 0 || row >= height())
		return 0;

	t_i32 count = 0;
	for(const t_pixel *p = this->row(row), *q = this->row(row) + width(); p < q; ++p)
		if(IS_BLACK(*p))
			++count;
	return count;
}

t_i32 grayimage::bw_col_blacks(t_i32 col) const throwempty
{
	if(col < 0 || col >= width())
		return 0;

	t_i32 count = 0;
	for(const t_pixel *p = begin() + col, *q = end(); p < q; p += width())
		if(IS_BLACK(*p))
			++count;
	return count;
}

t_i32 grayimage::bw_row_degree(t_i32 row) const throwempty
{
	if(row < 0 || row >= height())
		return 0;

	t_i32 count = 0;
	const t_pixel *p = this->row(row);
	const t_pixel *q = this->row(row) + width() - 1;
	for(; p < q; ++p)
		if(IS_BLACK(*p) && IS_WHITE(*(p + 1)))
			++count;
	if(IS_BLACK(*p))
		++count;
	return count;	
}

t_i32 grayimage::bw_col_degree(t_i32 col) const throwempty
{
	if(col < 0 || col >= width())
		return 0;

	t_i32 count = 0;
	const t_pixel *p = begin() + col;
	const t_pixel *q = end() - width();
	for(; p < q; p += width())
		if(IS_BLACK(*p) && IS_WHITE(*(p + width())))
			++count;
	if(IS_BLACK(*p))
		++count;
	return count;
}

////////////////////////////////////////////////////////////////////////////////////////////////////
}
