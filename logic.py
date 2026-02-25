import asyncio

async def merge(l, r):
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    
    result.extend(l[i:])
    result.extend(r[j:])
    return result
    
async def m_srot(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    lt, rt = await asyncio.gather(
        m_srot(arr[:mid]),
        m_srot(arr[mid:])
    )
    
    return await merge(lt, rt)

