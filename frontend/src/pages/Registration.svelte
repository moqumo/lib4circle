<script lang="ts">
    let isbn = '';
    let bookInfo = null;

    function handleInput(event) {
        const value = event.target.value;
        if (value.length > 13) {
            isbn = value.slice(0, 13);
        } else {
            isbn = value;
        }
    }

    async function fetchBookInfo() {
        if (isbn.length === 13) {
            console.log("fetchBookInfo");
            try {
                const response = await fetch(`https://api.openbd.jp/v1/get?isbn=${isbn}`);
                if (response.ok) {
                    const data = await response.json();
                    console.log(data);
                    if (data[0]) {
                        const book = data[0].summary;
                        bookInfo = {
                            title: book.title,
                            creator: book.author,
                            publisher: book.publisher
                        };
                    } else {
                        bookInfo = { error: '書籍情報が見つかりませんでした。' };
                    }
                } else {
                    console.error('Network response was not ok:', response.statusText);
                    bookInfo = { error: `書籍情報が見つかりませんでした。ステータスコード: ${response.status}` };
                }
            } catch (error) {
                console.error('Fetch error:', error);
                bookInfo = { error: `書籍情報の取得中にエラーが発生しました。エラーメッセージ: ${error.message}` };
            }
        } else {
            bookInfo = { error: '有効なISBNを入力してください。' };
        }
        console.log(bookInfo);
    }

    async function isExists(){
        fetch(`$import.meta.env.VITE_API_URL/isbn/${isbn}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            if (response.ok) {
                const data = response.json();
                console.log(data);
                return data;
            } else {
                throw new Error('Network response was not ok');
            }
        });
    }
</script>

<p>ISBNを入力してください</p>
<input
    class="isbn"
    type="text"
    id="isbn"
    name="isbn"
    placeholder="ISBN"
    required
    bind:value={isbn}
    on:input={handleInput}
/>
<button type="button" on:click={fetchBookInfo}>検索</button>

<button type="button" on:click={isExists}>確認</button>

{#if bookInfo}
    {#if bookInfo.error}
        <p>{bookInfo.error}</p>
    {:else}
        <div>
            <h2>{bookInfo.title}</h2>
            <p>{bookInfo.creator}</p>
            <p>{bookInfo.publisher}</p>
        </div>
    {/if}
{/if}

<style>
    .isbn {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        box-sizing: border-box;
    }
    img {
        max-width: 100px;
        height: auto;
    }
</style>